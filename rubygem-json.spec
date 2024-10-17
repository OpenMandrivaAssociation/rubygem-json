Summary:	JSON Implementation for Ruby
Name:		rubygem-json
Version:	2.6.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://flori.github.com/json
Source0:	http://rubygems.org/gems/json-%{version}.gem
BuildRequires:	ruby
BuildRequires:	ruby-devel
%rename		ruby-%{gem_name}

%description
This is a JSON implementation as a Ruby extension in C.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
%gem_build

%install
%gem_install

%files
%gem_files
