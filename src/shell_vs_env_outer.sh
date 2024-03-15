# shell_vs_env_outer.sh
window="neighbor"
threshold=0.5

echo "outer: window is ${window} and threshold is ${threshold}"
bash src/shell_vs_env_inner.sh
