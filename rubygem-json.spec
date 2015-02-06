%define	rbname	json

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.8.1
Release:	5
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
rm -rf %{buildroot}%{gem_dir}/gems/%{rbname}-%{version}/ext

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}
%{gem_dir}/gems/%{rbname}-%{version}/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/data
%{gem_dir}/gems/%{rbname}-%{version}/data/*.html
%{gem_dir}/gems/%{rbname}-%{version}/data/*.js
%{gem_dir}/gems/%{rbname}-%{version}/data/*.json
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/json.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/json
%{gem_dir}/gems/%{rbname}-%{version}/lib/json/*
%dir %{gem_dir}/gems/%{rbname}-%{version}/tools
%{gem_dir}/gems/%{rbname}-%{version}/tools/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
%dir %{ruby_sitearchdir}/json
%dir %{ruby_sitearchdir}/json/ext
%{ruby_sitearchdir}/json/ext/generator.so
#{ruby_sitearchdir}/json/ext/parser.so

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}
%doc %{gem_dir}/gems/%{rbname}-%{version}/README.*
%dir %{gem_dir}/gems/%{rbname}-%{version}/tests
%{gem_dir}/gems/%{rbname}-%{version}/tests/*


