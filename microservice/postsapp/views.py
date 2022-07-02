from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from .utils import fetch_post, valid_user


class PostListView(ListCreateAPIView):
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response({"posts": serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        # somehow throws KeyError when userId is not provided... it even passes through validation
        # fixed by this if below
        if "userId" in request.data:
            if serializer.is_valid():
                # user validation via external api
                if not valid_user(request.data['userId']):
                    return Response("Forbidden", status=status.HTTP_403_FORBIDDEN)
                serializer.save()
                return Response("Successfully created", status=status.HTTP_201_CREATED)
        return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)


class PostDetailViewID(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get(self, request, **kwargs):
        id = self.kwargs['id']  # from URL
        try:
            post = Post.objects.get(pk=id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            post = fetch_post(id)  # fetch post from external api
            if post is not None:
                Post(id=id, userId=post['userId'], title=post['title'], body=post['body']).save()
                return Response(post)
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, **kwargs):
        id = self.kwargs['id']  # from URL
        try:
            post = Post.objects.get(pk=id)
            # all fields are required (except userId, id)
            if 'body' not in request.data or 'title' not in request.data:
                return Response("Bad format", status=status.HTTP_400_BAD_REQUEST)
            # userId stays the same
            Post(id=id, userId=post.userId, title=request.data['title'],
                 body=request.data['body']).save()
            return Response("Edited successfully", status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None, **kwargs):
        id = self.kwargs['id']  # from URL
        try:
            post = Post.objects.get(pk=id)
            # not all fields are required
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response("Partially updated", status=status.HTTP_201_CREATED)
            return Response("Bad format", status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, **kwargs):
        id = self.kwargs['id']  # from URL
        try:
            Post.objects.get(pk=id).delete()
            return Response("Deleted successfully", status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)


class PostDetailViewUID(RetrieveAPIView):
    serializer_class = PostSerializer

    def get(self, request, **kwargs):
        uid = self.kwargs['uid']  # from URL
        post = Post.objects.all().filter(userId=uid)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
