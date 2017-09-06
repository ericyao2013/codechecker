# -------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -------------------------------------------------------------------------
"""
Helpers for determining triple arch of a compile action
"""

import shlex

from libcodechecker.analyze.analyzers import analyzer_base


def get_compile_command(action, config, source='', output=''):
    """ Generate a standardized and cleaned compile command serving as a base
    for other operations. """

    cmd = [config.analyzer_binary]
    cmd.extend(action.compiler_includes)
    if len(config.compiler_resource_dir) > 0:
        cmd.extend(['-resource-dir', config.compiler_resource_dir,
                    '-isystem', config.compiler_resource_dir])
    cmd.append('-c')
    if config.compiler_sysroot:
        cmd.extend(['--sysroot', config.compiler_sysroot])
    for path in config.system_includes:
        cmd.extend(['-isystem', path])
    for path in config.includes:
        cmd.extend(['-I', path])
    cmd.extend(['-x', action.lang])
    cmd.append(config.analyzer_extra_arguments)
    cmd.extend(action.analyzer_options)
    if output:
        cmd.extend(['-o', output])
    if source:
        cmd.append(source)
    return cmd


def get_triple_arch(action, source, config, env):
    """Returns the architecture part of the target triple for the given
    compilation command. """

    cmd = get_compile_command(action, config, source)
    cmd.insert(1, '-###')
    cmdstr = ' '.join(cmd)
    _, stdout, stderr = analyzer_base.SourceAnalyzer.run_proc(cmdstr, env)
    last_line = (stdout + stderr).splitlines()[-1]
    res_cmd = shlex.split(last_line)
    arch = ""
    i = 0
    while i < len(res_cmd) and res_cmd[i] != "-triple":
        i += 1
    if i < (len(res_cmd) - 1):
        arch = res_cmd[i + 1].split("-")[0]
    return arch
