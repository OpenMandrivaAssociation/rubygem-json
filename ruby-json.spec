%define	oname	json

Summary:	GeoIP ruby gem
Name:		ruby-%{oname}
Version:	1.2.0
Release:	%mkrel 1
License:	Ruby or GPLv2
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems ruby-devel ruby-rake
Requires:	ruby

%description
This is a implementation of the JSON specification according
to RFC 4627 in Ruby.
You can think of it as a low fat alternative to XML,
if you want to store data to disk or transmit it over
a network rather than use a verbose markup language.

%prep

%build

%install
rm -rf %{buildroot}
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

chmod g-w,g+r,o+r -R %{buildroot}

mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/*_json.rb
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

