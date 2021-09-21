sepblock=-------------------------------------------------------------------
newblock="$(sepblock)\n$(shell date -u) - $(shell git config user.name) <$(shell git config user.email)>\n\n-\n"

vc:
	@echo -e $(newblock) | cat - aws-regions.changes > aws-regions.changes.bak && mv aws-regions.changes.bak aws-regions.changes ||:
	@${VISUAL} +4 aws-regions.changes ||:
	@echo "Changes file updated." ||:
