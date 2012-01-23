%define	rbname	json

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.6.5
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://flori.github.com/json
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	rubygem(rake)
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
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks
%{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*
