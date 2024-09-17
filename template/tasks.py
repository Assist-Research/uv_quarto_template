from invoke import task


@task
def check(c):
    c.run("pre-commit run --all-files")
