import pytest
from Python_Package_Project import render_youtube, get_time_info, InvalidURLException

good_URL = [
    ("https://youtu.be/Nq4Mh_jTubA", 0),
    ("https://youtu.be/Nq4Mh_jTubA?t=62s", 62),
    ("https://www.youtube.com/watch?v=Nq4Mh_jTubA", 0),
]

bad_URL = [
    ("https://www.youtube.com/watch?v=Nq4Mh_jTubAbhishek"),
    ("https://www.youtube.com/watch?v=Nq4Mh_jTubA&t"),
    ("https://www.youtube.com/watch?v=Nq4Mh_jTubA&t==2s"),
    ("https://www.youtube.com/watch?v==Nq4Mh_jTubA&t=2s"),
]


@pytest.mark.parametrize("URL, response", good_URL)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response


@pytest.mark.parametrize("URL", bad_URL)
def test_get_time_info_fail(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)
