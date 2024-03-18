include lib/tut/tutorial.mk

SRC_FILES := $(wildcard src/*.sh)
SRC_EXCLUDE := \
	src/env_var_inner.sh \
	src/shell_var_inner.sh
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

out/change_path.out: src/change_path.sh
	bash $< > $@

out/env_var_outer.out: src/env_var_outer.sh src/env_var_inner.sh
	bash $< > $@

out/env_var_py.out: src/env_var_py.sh src/env_var_py.py
	bash $< > $@

out/flush.out: src/flush.py
	python $< > $@

out/fork_exec.out: src/fork_exec.py
	python $< > $@

out/shell_var_outer.out: src/shell_var_outer.sh src/shell_var_inner.sh
	bash $< > $@

out/show_env_vars.out: src/show_env_vars.sh
	bash $< > $@

out/show_path.out: src/show_path.sh
	bash $< | grep -v ruby | grep -v nightly | grep -v draw.io | sed -e 's/gregwilson/tut/' > $@
