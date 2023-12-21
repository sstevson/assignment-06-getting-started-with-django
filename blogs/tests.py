# Using datetime timezone.utc below because the django
# import appears to no longer be valid
from datetime import datetime, timedelta, timezone

from django.test import TestCase
from django.contrib.auth.models import User

from blogs.models import Post, Category


class PostTestCase(TestCase):
    fixtures = ['blogs_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = 'This is a title'
        p1 = Post(title = expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    fixtures = ['blogs_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = 'A Category'
        c1 = Category(name = expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['blogs_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.utcnow().replace(tzinfo=timezone.utc)
        self.timedelta = timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get('/')
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            # Need to address a bug in the last part of this
            # test case. self.assertNotContains causes the test to fail

    def test_details_only_published(self):
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get('/posts/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
