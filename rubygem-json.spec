%define	gem_name	json
%define _enable_debug_packages 1

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
%autosetup -n %{gem_name}-%{version}

%build
%gem_build 


#rm -rf %{buildroot}%{gem_dir}/%{gem_name}-%{version}/ext
#-f '(.*.rb|benchmarks|bin|data|java/lib|tools|tests)'

%install
cp -r %{_builddir}/%{gem_name}-%{version}/usr %{buildroot} 


#rm -rf %{buildroot}%{gem_dir}/%{gem_name}-%{version}/ext

%files
%{_libdir}/ruby/gems/*/specifications/%{gem_name}-%{version}.gemspec
%{_libdir}/ruby/gems/*/cache/%{gem_name}-%{version}.gem
%{_libdir}/ruby/gems/*/gems/%{gem_name}-%{version}
%{_libdir}/ruby/gems/*/extensions/*/*/%{gem_name}-%{version}


%files doc
%doc %{ruby_gemdir}/doc/%{gem_name}-%{version}/
%doc %{ruby_gemdir}/gems/%{gem_name}-%{version}/README.*

#usr/lib64/ruby/gems/2.7.0/gems/json-2.6.1
