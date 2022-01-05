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
%autosetup -n %{gem_name}-%{version}

%build
%gem_build 

%install
cp -r %{_builddir}/%{gem_name}-%{version}/usr %{buildroot} 

%files
%{_libdir}/ruby/gems/*/specifications/%{gem_name}-%{version}.gemspec
%{_libdir}/ruby/gems/*/cache/%{gem_name}-%{version}.gem
%{_libdir}/ruby/gems/*/gems/%{gem_name}-%{version}
%{_libdir}/ruby/gems/*/extensions/*/*/%{gem_name}-%{version}

%files doc
%doc %{ruby_gemdir}/doc/%{gem_name}-%{version}/
%doc %{ruby_gemdir}/gems/%{gem_name}-%{version}/README.*

