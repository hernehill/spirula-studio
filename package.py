name = 'spirula'

version = '2026.10.16.hh.1.0.0'

authors = [
    'Harry (J.X.) C.',
]

description = '''Gaussian Splat train'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']
    c.plugins.release_hook.hh_emailer.recipients = []

    # This package will ignore build_* nativaley.
    # So, if we use our _rez_build default, the build will fail.
    c.build_directory = "build_rez"

requires = [
    "vulkanSDK",
]

private_build_requires = [
]

variants = [
]


# ------------------------------------------
# Build with:
# rez-build -- -DSS_BACKEND=vulkan -DSS_ENABLE_PATENTED=ON -DGLFW_BUILD_WAYLAND=OFF
# rez-release -- -DSS_BACKEND=vulkan -DSS_ENABLE_PATENTED=ON -DGLFW_BUILD_WAYLAND=OFF


def commands():
    env.REZ_SPIRULA_ROOT = '{root}'
    env.PATH.append('{root}/bin')


uuid = 'repository.spirula-studio'
