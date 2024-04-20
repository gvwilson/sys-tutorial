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

${OUT}/socket_client.out: ${SRC}/socket_client.py ${RUN2}
	${RUN2} "${SITE_SERVER}" "python $<" > $@

${OUT}/socket_server.out: ${SRC}/socket_server.py ${SRC}/socket_server_client.py ${RUN2}
	${RUN2} "python $<" "python ${SRC}/socket_server_client.py" > $@
