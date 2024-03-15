include lib/tut/tutorial.mk

SRC_FILES := $(wildcard src/*.sh)
SRC_EXCLUDE := \
	src/shell_vs_env_inner.sh
OUT_FILES := $(patsubst src/%.sh,out/%.out,$(filter-out ${SRC_EXCLUDE},${SRC_FILES}))

LINT_OTHER_PAGES := 
LINT_OTHER_FILES := 

## release: create a release
.PHONY: release
release:
	@rm -rf sys-tutorial.zip
	@zip -r sys-tutorial.zip \
	${SRC} \
	${OUT} \
	-x \*~

## run: re-run examples
.PHONY: run
run: ${OUT_FILES}

out/flush.out: src/flush.py
	python $< > $@

out/shell_vs_env_outer.out: src/shell_vs_env_outer.sh src/shell_vs_env_inner.sh
	bash $< > $@
