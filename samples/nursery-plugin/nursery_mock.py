import pkg_resources

import click

from nursery.context import DEFAULT_CONTEXT_SETTINGS
from nursery.context import pass_context
from nursery.context import attach_target
from nursery.targets import TargetPlugin


short_name = "mock"
version = pkg_resources.get_distribution(f"nursery-{short_name}").version


class MockTarget(TargetPlugin):
    """Mock Custom Target
    """

    name = "Nursery mock Target"
    description = "This the included Nursery Plugin for the mock Target"
    short_name = short_name

    def up(self, size=None):
        """The real `up` for this env
        """
        if size:
            self.set_size(size)

    def destroy(self):
        pass

    def halt(self):
        pass

    def cp(self, source, target):
        print(f"Copy {source} to {target} here")
        pass

    def ssh(self):
        pass

    def set_size(self, size):
        """Set the drive size.
        """
        pass

    def on_setup_env(self):
        pass


@click.group(short_name)
@click.version_option(prog_name=MockTarget.name, version=version)
@pass_context
@attach_target
def cli(ctx):  # Entry point command for this target.
    """Control a VirtualBox instance.
    """
    # Find the target once and attach it to the ctx so we can easily use it later.
    pass


@cli.command("cp", context_settings=DEFAULT_CONTEXT_SETTINGS)
@click.argument("source")
@click.argument("target")
@pass_context
def cp_cmd(ctx, source, target):
    """Copy  files or directories. Accepts two args in one of the
    following forms:

    <local_path> <remote_path>

    <local_path> :<remote_path>

    :<remote_path> <local_path>

    <local_path> [vm_name]:<remote_path>

    [vm_name]:<remote_path> <local_path>

    For example: `nursery mock cp localfile.txt remotefile.txt`
    """
    print("IN CP")
    ctx.target.cp(source, target)


@cli.command("destroy")
@pass_context
def destroy_cmd(ctx):
    ctx.target.destroy()


@cli.command("halt")
@pass_context
def halt_cmd(ctx):
    ctx.target.halt()


@cli.command("ssh")
@pass_context
def ssh_cmd(ctx):
    ctx.target.ssh()


@cli.command("up")
@pass_context
def up_cmd(ctx):
    ctx.target.up()


@cli.command("resize")
@pass_context
def resize_cmd(ctx):
    """Resize the size of the instance's disk.
    """
    ctx.target.set_size()
