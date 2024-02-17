include lib/tut/tutorial.mk
include depend.mk

PAGE := pages/index.md
RUN2 := bin/silent.sh bin/run2.sh
SITE_SERVER := python -m http.server -d site

## release: create a release
.PHONY: release
release:
	@rm -rf web-tutorial.zip
	@zip -r web-tutorial.zip \
	src \
	out \
	-x \*~

PY_FILES := $(wildcard ${SRC}/*.py)
PY_EXCLUDED := ${SRC}/headers.py ${SRC}/socket_server_client.py
OUT_FILES := $(patsubst ${SRC}/%.py,${OUT}/%.out,$(filter-out ${PY_EXCLUDED},${PY_FILES}))

## run: re-run all examples
.PHONY: run
run: ${OUT_FILES}

${OUT}/get_local_motto.out: ${SRC}/get_local_motto.py ${RUN2}
	${RUN2} "${SITE_SERVER}" "python $<" > $@

${OUT}/get_json.out: ${SRC}/get_json.py
	python $< > $@

${OUT}/get_motto.out: ${SRC}/get_motto.py
	python $< > $@

${OUT}/get_nonexistent.out: ${SRC}/get_nonexistent.py
	python $< > $@

${OUT}/https_client.out: ${SRC}/https_client.py ${SRC}/headers.py
	python $< > $@

${OUT}/show_response_headers.out: ${SRC}/show_response_headers.py
	python $< > $@

${OUT}/socket_client.out: ${SRC}/socket_client.py ${RUN2}
	${RUN2} "${SITE_SERVER}" "python $<" > $@

${OUT}/socket_server.out: ${SRC}/socket_server.py ${SRC}/socket_server_client.py ${RUN2}
	${RUN2} "python $<" "python ${SRC}/socket_server_client.py" > $@
