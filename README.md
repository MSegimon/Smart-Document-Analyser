# Smart-Document-Analyser Queue Implementation

The difference between this and the main project is that this enqueues all the main calls for file processing and text analysis. This is done to ensure that the main thread is not blocked and can continue to process other requests. The main differences are in the `main.py` file where the main calls are enqueued and in `fileFunctions.py` and `textAnalysisFunctions.py` where the calls are dequeued and processed.
