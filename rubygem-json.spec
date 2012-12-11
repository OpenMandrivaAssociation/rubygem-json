%define	rbname	json

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.6.6
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://flori.github.com/json
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
%rename		ruby-%{rbname}

%description
This is a JSON implementation as a Ruby extension in C.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(.*.rb|benchmarks|bin|data|java/lib|tools|tests)'

%install
%gem_install
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{rbname}-%{version}/ext

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/data
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.html
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.js
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.json
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tools
%{ruby_gemdir}/gems/%{rbname}-%{version}/tools/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%dir %{ruby_sitearchdir}/json
%dir %{ruby_sitearchdir}/json/ext
%{ruby_sitearchdir}/json/ext/generator.so
%{ruby_sitearchdir}/json/ext/parser.so

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README.*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*


%changelog
* Mon Apr 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6.6-1
+ Revision: 789986
- version update 1.6.6

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.5-3
+ Revision: 774413
- drop rake dependency, it's now provided by ruby
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6.5-1
+ Revision: 766962
- version update 1.6.5

  + Andrey Smirnov <asmirnov@mandriva.org>
    - rpmlint warning

* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.1-1
+ Revision: 643352
- regenerate spec with gem2rpm5
- new release: 1.5.1

* Sat Dec 04 2010 Rémy Clouard <shikamaru@mandriva.org> 1.4.6-2mdv2011.0
+ Revision: 609255
- %gem_build macros are broken at the moment, using classic method from
  gem2rpm to build the package for the moment.

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - use %%rename macro
    - use new %%gem_* macros

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-2mdv2010.1
+ Revision: 500558
- don't install the gem itself or any of the build files...
- rename to follow naming scheme for ruby gem packages
- rename to follow ruby gem naming scheme...

* Mon Feb 01 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 499318
- add missing buildrequires
- import ruby-json

