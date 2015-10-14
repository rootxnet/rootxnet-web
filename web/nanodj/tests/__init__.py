from os.path import join, dirname, abspath
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template import Context
from django.test import override_settings, Client, TestCase
from django.http import Http404

from ..views import get_page_or_404, page


@override_settings(
    PAGE_BUILD_DIR=join(dirname(abspath(__file__)), "_build_outer", "_build_inner"),
)
class NanoTest(TestCase):
    def test_get_page_or_404(self):
        # check if the file was properly loaded
        t1 = get_page_or_404("test.html")
        r = t1["html"].render(Context())
        self.assertInHTML(r, "INNER_1234567890")

        with self.assertRaises(Http404):
            get_page_or_404("nonexistent.html")

        # this file exists but the path traversal was attempted
        # which should internally raise SuspiciousFileOperation,
        # then Http404
        with self.assertRaises(Http404):
            get_page_or_404("../test.html")

    def test_page(self):
        client = Client()

        # test if proper request goes thru
        req1 = client.get(reverse(page, kwargs={"slug": "test"}))
        self.assertEqual(req1.status_code, 200)

        # test if the template was properly included
        self.assertContains(req1, "INNER_1234567890")

        # test bad request
        req2 = client.get(reverse(page, kwargs={"slug": "nonexistent"}))
        self.assertEqual(req2.status_code, 404)

    def test_url_path_traversal(self):
        """
        Check against multiple forms of path traversal hacks on URL resolver level
        """
        client = Client()

        # protect from directory traversing
        with self.assertRaises(NoReverseMatch):
            client.get(reverse(page, kwargs={"slug": "../test"}))

        # protect from absolute path hack
        with self.assertRaises(NoReverseMatch):
            client.get(reverse(page, kwargs={"slug": "/test"}))
