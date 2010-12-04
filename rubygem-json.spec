%define oname json

Name:       rubygem-%{oname}
Version:    1.4.6
Release:    %mkrel 1
Summary:    JSON Implementation for Ruby
Group:      Development/Ruby
License:    GPLv2+ or Ruby License
URL:        http://flori.github.com/json
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
Provides:   rubygem(%{oname}) = %{version}

%description
This is a JSON implementation as a Ruby extension in C.


%prep

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
cp -ax .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}

#Move arch-dependant files to sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}/
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/json/ext/json/ext/*.so \
   %{buildroot}%{ruby_sitearchdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

# Install executables
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/edit_json.rb
%{_bindir}/prettify_json.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so
