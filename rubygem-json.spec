%define	gem_name	json
%global _empty_manifest_terminate_build 0

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
%autosetup -p1 -n %{gem_name}-%{version}

%build
%gem_build

%install
%gem_install -d %{buildroot}

%files
%{ruby_gemdir}/gems/json-%{version}
%{ruby_gemdir}/extensions/*/*/json-%{version}
%{ruby_gemdir}/cache/json-%{version}.gem
%{ruby_gemdir}/specifications/json-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/json-%{version}
