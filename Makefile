include lib/tut/tutorial.mk

PY_FILES := $(wildcard ${SRC}/*.py)
PY_EXCLUDED := ${SRC}/headers.py
OUT_FILES := $(patsubst ${SRC}/%.py,${OUT}/%.out,$(filter-out ${PY_EXCLUDED},${PY_FILES}))
LINT_OTHER_PAGES := 
LINT_OTHER_FILES := site/server_first_cert.pem

PORT := 8000
RUNNER := bin/runner.sh
SITE_SERVER := python -m http.server -d site ${PORT}

## release: create a release
.PHONY: release
release:
	@rm -rf safety-tutorial.zip
	@zip -r safety-tutorial.zip \
	src \
	out \
	-x \*~

## listen: listen on port 8000
.PHONY: listen
listen:
	nc -l -p ${PORT}

## run: re-run all examples
.PHONY: run
run: ${OUT_FILES}

${OUT}/birds_head.out: ${SRC}/birds_head.sh
	bash $< > $@

${OUT}/dump_structure.out: ${SRC}/dump_structure.py
	python $< | grep -e '< ' | sed -e 's/< //g' > $@

${OUT}/get_404.out: ${SRC}/get_404.py
	python $< > $@

${OUT}/get_json.out: ${SRC}/get_json.py
	python $< > $@

${OUT}/get_local.out: ${SRC}/get_local.py ${RUNNER}
	${RUNNER} ${PORT} "${SITE_SERVER}" "python $<" &> $@

${OUT}/get_remote.out: ${SRC}/get_remote.py
	python $< > $@

${OUT}/response_headers.out: ${SRC}/response_headers.py
	python $< > $@

${OUT}/run_lsof.out: ${SRC}/run_lsof.sh
	bash $< > $@
