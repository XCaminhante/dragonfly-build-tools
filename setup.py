setup_args = dict(name="df2",
                  version="0.1",
                  url="https://github.com/operasoftware/dragonfly-build-tools",
                  author="Christian Krebs, Rune Halvorsen",
                  author_email="chrisk@opera.com",
                  description="Tools for Opera Dragonfly development.",
                  data_files=[("df2", ["df2/DEFAULTS",
                                       "df2/CONFIGDOC"]),
                              ("df2/codegen/resources/style", ["df2/codegen/resources/style/style.css",
                                                               "df2/codegen/resources/style/arrow.png",
                                                               "df2/codegen/resources/style/favicon.ico",
                                                               "df2/codegen/resources/style/img-press-logo.png"]),
                              ("df2/codegen/resources/script", ["df2/codegen/resources/script/script.js"])],
                  packages=["df2", "df2.codegen"],
                  zip_safe=False)

try:
    from setuptools import setup
    setup_args["entry_points"] = dict(console_scripts=["df2=df2.df2:main"])

except ImportError:
    from distutils.core import setup

setup(**setup_args)
