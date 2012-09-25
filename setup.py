import sys

kwargs={}

# fall back on no plugin-extensions and no dependency handling if setuptools 
# is not installed.
try:
    from setuptools import setup
    kwargs["install_requires"]=['rdflib', 'html5lib']

    # simplejson needed if the JSON serialization is used and 
    # if the underlying python version is 2.5 or lower
    if sys.version_info.major==2 and sys.version_info.minor<6:
        kwargs["install_requires"].append("simplejson")
        
    kwargs["entry_points"]={
        'rdf.plugins.parser' : [ 'rdfa = pyRdfa.rdflib:RDFaParser',
                                 'rdfa1.1 = pyRdfa.rdflib:RDFaParser',
                                 'application/xhtml+xml = pyRdfa.rdflib:RDFaParser',
                                 'application/svg+xml = pyRdfa.rdflib:RDFaParser',
                                 'html = pyRdfa.rdflib:StructuredDataParser',
                                 'text/html = pyRdfa.rdflib:StructuredDataParser',
                                 ]
        }

except:
    from distutils.core import setup

setup(name="pyRdfa",
      description="pyRdfa Libray",
      version="3.4.3",
      author="Ivan Herman",
      author_email="ivan@w3.org",
      maintainer="Ivan Herman",
      maintainer_email="ivan@w3.org",
      packages=['pyRdfa',
				'pyRdfa.transform',
				'pyRdfa.extras',
				'pyRdfa.rdfs',
				'pyRdfa.host',
				'pyRdfaExtras',
				'pyRdfaExtras.extras',
				'pyRdfaExtras.serializers'
				], 
      **kwargs)

