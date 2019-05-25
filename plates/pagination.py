from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response


class CustomPaginationWithoutCount(PageNumberPagination):
    """
    We create a custom pagination class to remove the count
    """

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('total_pages', self.page.paginator.num_pages),
            ('results', data)
        ]))
