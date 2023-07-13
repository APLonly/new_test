import pytest
from Python_Package_Project import render_youtube, InvalidURLException


class Testyoutube:
    good_URL = [
        ("https://youtu.be/Nq4Mh_jTubA", "sucess"),
        ("https://youtu.be/Nq4Mh_jTubA?t=62s", "sucess"),
        ("https://www.youtube.com/watch?v=Nq4Mh_jTubA", "sucess"),
    ]

    bad_URL = [
        ("https://www.youtube.com/watch?v=Nq4Mh_jTubAbhishek"),
        ("https://www.youtube.com/watch?v=Nq4Mh_jTubA&t"),
        ("https://www.youtube.com/watch?v=Nq4Mh_jTubA&t==2s"),
        ("https://www.youtube.com/watch?v==Nq4Mh_jTubA&t=2s"),
    ]

    @pytest.mark.parametrize("URL, response", good_URL)
    def test_render_youtube_video(self, URL, response):
        assert render_youtube(URL) == response

    @pytest.mark.parametrize("URL", bad_URL)
    def test_render_youtube_video_fail(self, URL):
        with pytest.raises(InvalidURLException):
            render_youtube(URL)
