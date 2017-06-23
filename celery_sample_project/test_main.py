import unittest
import mock
import main


class TestTranscodeCase(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = main.app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    @mock.patch('main.transcode_360p.apply_async')
    def test_transcode_360p(self, mock_transcode_360p):
        # you can manipulate the return value if needed
        mock_transcode_360p.return_value = "360p"
        self.app.post('/transcode360p')
        # check if the arguments are right and it was called once
        mock_transcode_360p.assert_called_once_with(queue='tasks', priority=1)

    @mock.patch('main.transcode_480p.apply_async')
    def test_transcode_480p(self, mock_transcode_480p):
        self.app.post('/transcode480p')
        mock_transcode_480p.assert_called_once_with(queue='tasks', priority=2)

    @mock.patch('main.transcode_720p.apply_async')
    def test_transcode_720p(self, mock_transcode_720p):
        self.app.post('/transcode720p')
        mock_transcode_720p.assert_called_once_with(queue='tasks', priority=3)

    @mock.patch('main.end_processing.signature')
    @mock.patch('main.transcode_360p.signature')
    @mock.patch('main.transcode_480p.signature')
    @mock.patch('main.transcode_720p.signature')
    @mock.patch('main.transcode_1080p.signature')
    def test_transcodeToALL_tasks(self, mock_transcode_1080p, mock_transcode_720p,
                                  mock_transcode_480p, mock_transcode_360p,
                                  mock_endprocessing):
        self.app.post('/transcodeALL')
        mock_transcode_1080p.assert_called_once_with(queue='tasks', priority=1, immutable=True)
        mock_transcode_720p.assert_called_once_with(queue='tasks', priority=2, immutable=True)
        mock_transcode_480p.assert_called_once_with(queue='tasks', priority=3, immutable=True)
        mock_transcode_360p.assert_called_once_with(queue='tasks', priority=4, immutable=True)
        mock_endprocessing.assert_called_once_with(queue='tasks', immutable=True)

    @mock.patch('main.chord')
    def test_transcodeToALL_chord(self, mock_chord):
        self.app.post('/transcodeALL')
        transcoding_tasks = main.group(
            main.transcode_1080p.signature(queue='tasks', priority=1, immutable=True),
            main.transcode_720p.signature(queue='tasks', priority=2, immutable=True),
            main.transcode_480p.signature(queue='tasks', priority=3, immutable=True),
            main.transcode_360p.signature(queue='tasks', priority=4, immutable=True)
        )
        # main.end_processing.signature(queue='tasks', immutable=True) -- Not used in chord?!
        mock_chord.assert_called_once_with(transcoding_tasks)

    @mock.patch('main.chord')
    @mock.patch('main.group')
    def test_transcodeToALL_group(self, mock_group, mock_chord):
        self.app.post('/transcodeALL')
        mock_group.assert_called_once_with(
            main.transcode_1080p.signature(queue='tasks', priority=1, immutable=True),
            main.transcode_720p.signature(queue='tasks', priority=2, immutable=True),
            main.transcode_480p.signature(queue='tasks', priority=3, immutable=True),
            main.transcode_360p.signature(queue='tasks', priority=4, immutable=True)
        )


if __name__ == '__main__':
    unittest.main()
