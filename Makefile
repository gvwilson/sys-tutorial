include lib/mccole/mccole.mk

## run: re-run examples
.PHONY: run
run: ${OUT_FILES}

out/change_path.out: src/change_path.sh
	bash $< > $@

out/chroot_example.out: src/chroot_example.sh
	bash $< >& $@

out/env_var_outer.out: src/env_var_outer.sh src/env_var_inner.sh
	bash $< > $@

out/env_var_py.out: src/env_var_py.sh src/env_var_py.py
	bash $< > $@

out/flush.out: src/flush.py
	python $< > $@

out/fork_exec.out: src/fork_exec.py
	python $< > $@

out/interpolate.out: src/interpolate.sh
	bash $< > $@

out/shell_var_outer.out: src/shell_var_outer.sh src/shell_var_inner.sh
	bash $< > $@

out/show_env_vars.out: src/show_env_vars.sh
	bash $< > $@

out/show_path.out: src/show_path.sh
	bash $< | grep -v ruby | grep -v nightly | grep -v draw.io | sed -e 's/gregwilson/tut/' > $@

out/show_virtual_env.out: src/show_virtual_env.sh
	bash $< | sed -e 's/gregwilson/tut/' > $@
