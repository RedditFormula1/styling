language: node_js
node_js:
  - "stable"
script: "gulp build"
matrix:
	allow_failures:
		- node: stable
