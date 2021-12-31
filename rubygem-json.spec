%define	gem_name	json

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{gem_name}

Version:	2.6.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://flori.github.com/json
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
%rename		ruby-%{gem_name}

%description
This is a JSON implementation as a Ruby extension in C.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
#cd %{rbname}-%{version}
%gem_build -f '(.*.rb|benchmarks|bin|data|java/lib|tools|tests)'

%install
#%%gem_install
/usr/bin/gem install json-2.6.1.gem -V --local --env-shebang --document rdoc,ri --force --ignore-dependencies --install-dir /usr/share/ruby/gems --bindir /usr/bin --build-root . -f '(.*.rb|benchmarks|bin|data|java/lib|tools|tests)'
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/ext

%files
%dir %{gem_dir}/gems/%{gem_name}-%{version}
%{gem_dir}/gems/%{gem_name}-%{version}/*.rb
%dir %{gem_dir}/gems/%{gem_name}-%{version}/data
%{gem_dir}/gems/%{gem_name}-%{version}/data/*.html
%{gem_dir}/gems/%{gem_name}-%{version}/data/*.js
%{gem_dir}/gems/%{gem_name}-%{version}/data/*.json
%dir %{gem_dir}/gems/%{gem_name}-%{version}/lib
%{gem_dir}/gems/%{gem_name}-%{version}/lib/json.rb
%dir %{gem_dir}/gems/%{gem_name}-%{version}/lib/json
%{gem_dir}/gems/%{gem_name}-%{version}/lib/json/*
%dir %{gem_dir}/gems/%{gem_name}-%{version}/tools
%{gem_dir}/gems/%{gem_name}-%{version}/tools/*.rb
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%dir %{ruby_sitearchdir}/json
%dir %{ruby_sitearchdir}/json/ext
%{ruby_sitearchdir}/json/ext/generator.so
#{ruby_sitearchdir}/json/ext/parser.so

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_dir}/gems/%{gem_name}-%{version}/README.*
%dir %{gem_dir}/gems/%{gem_name}-%{version}/tests
%{gem_dir}/gems/%{gem_name}-%{version}/tests/*


