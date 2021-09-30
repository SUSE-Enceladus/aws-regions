sepblock=-------------------------------------------------------------------
newblock="$(sepblock)\n$(shell date -u) - $(shell git config user.name) <$(shell git config user.email)>\n\n-\n"

vc:
	@echo -e $(newblock) | cat - python3-aws-regions.changes > python3-aws-regions.changes.bak && mv python3-aws-regions.changes.bak python3-aws-regions.changes ||:
	@${VISUAL} +4 python3-aws-regions.changes ||:
	@echo "Changes file updated." ||:
