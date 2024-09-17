from invoke import task


@task
def check(c):
    c.run("pre-commit run --all-files")


@task
def docs(c):
    with c.cd("docs"):
        c.run("quartodoc build")
        c.run("quarto render")
    

@task
def publish(c):
    with c.cd("docs"):
        c.run("quarto publish netlify")
