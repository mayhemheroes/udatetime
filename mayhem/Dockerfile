# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

ADD . /src
WORKDIR /src
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y clang cmake make
RUN rm /usr/bin/x86_64-linux-gnu-gcc && ln -s /usr/bin/clang /usr/bin/x86_64-linux-gnu-gcc

ENV CC="/usr/bin/clang"
ENV CFLAGS="-fsanitize=fuzzer-no-link,undefined"
ENV CXX="/usr/bin/clang++"
ENV CXXFLAGS="-fsanitize=fuzzer-no-link,undefined"
RUN python3 -m pip install .

ENV LD_PRELOAD="${LD_PRELOAD}:/usr/local/lib/python3.9/dist-packages/ubsan_with_fuzzer.so"
CMD ["/src/mayhem/fuzz_time.py"]
