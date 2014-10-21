%define	rbname	json

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.8.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://flori.github.com/json
Source0:	http://rubygems.org/gems/json-1.8.1.gem
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
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/data
# %{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.html
# %{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.js
# %{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.json
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
# %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json.rb
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json
# %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/*
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tools
# %{ruby_gemdir}/gems/%{rbname}-%{version}/tools/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
# %dir %{ruby_sitearchdir}/json
%dir %{ruby_sitearchdir}/json/ext
%{ruby_sitearchdir}/json/ext/generator.so
# %{ruby_sitearchdir}/json/ext/parser.so
%{_datadir}/gems/doc/json-1.8.1/rdoc/BigDecimal.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Class.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Complex.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Date.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/DateTime.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Exception.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/CircularDatastructure.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Ext.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/GeneratorError.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/GenericObject.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/JSONError.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/MissingUnicodeSupport.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/NestingError.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/ParserError.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/Array.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/FalseClass.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/Float.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/Hash.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/Integer.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/NilClass.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/Object.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/String.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/String/Extend.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/GeneratorMethods/TrueClass.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Generator/State.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Parser.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/Pure/Parser/Encoding.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/JSON/UnparserError.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Kernel.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/OpenStruct.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/README_rdoc.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Range.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Rational.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Regexp.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Struct.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Symbol.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/Time.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/fonts.css
%{_datadir}/gems/doc/json-1.8.1/rdoc/fonts/Lato-Light.ttf
%{_datadir}/gems/doc/json-1.8.1/rdoc/fonts/Lato-LightItalic.ttf
%{_datadir}/gems/doc/json-1.8.1/rdoc/fonts/Lato-Regular.ttf
%{_datadir}/gems/doc/json-1.8.1/rdoc/fonts/Lato-RegularItalic.ttf
%{_datadir}/gems/doc/json-1.8.1/rdoc/fonts/SourceCodePro-Bold.ttf
%{_datadir}/gems/doc/json-1.8.1/rdoc/fonts/SourceCodePro-Regular.ttf
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/add.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/arrow_up.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/brick.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/brick_link.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/bug.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/bullet_black.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/bullet_toggle_minus.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/bullet_toggle_plus.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/date.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/delete.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/find.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/loadingAnimation.gif
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/macFFBgHack.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/package.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/page_green.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/page_white_text.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/page_white_width.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/plugin.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/ruby.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/tag_blue.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/tag_green.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/transparent.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/wrench.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/wrench_orange.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/images/zoom.png
%{_datadir}/gems/doc/json-1.8.1/rdoc/index.html
%{_datadir}/gems/doc/json-1.8.1/rdoc/js/darkfish.js
%{_datadir}/gems/doc/json-1.8.1/rdoc/js/jquery.js
%{_datadir}/gems/doc/json-1.8.1/rdoc/js/navigation.js
%{_datadir}/gems/doc/json-1.8.1/rdoc/js/search.js
%{_datadir}/gems/doc/json-1.8.1/rdoc/js/search_index.js
%{_datadir}/gems/doc/json-1.8.1/rdoc/js/searcher.js
%{_datadir}/gems/doc/json-1.8.1/rdoc/rdoc.css
%{_datadir}/gems/doc/json-1.8.1/rdoc/table_of_contents.html
%{_datadir}/gems/doc/json-1.8.1/ri/BigDecimal/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/BigDecimal/cdesc-BigDecimal.ri
%{_datadir}/gems/doc/json-1.8.1/ri/BigDecimal/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/BigDecimal/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Class/cdesc-Class.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Complex/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Complex/cdesc-Complex.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Complex/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Complex/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Date/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Date/cdesc-Date.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Date/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Date/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/DateTime/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/DateTime/cdesc-DateTime.ri
%{_datadir}/gems/doc/json-1.8.1/ri/DateTime/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/DateTime/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Exception/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Exception/cdesc-Exception.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Exception/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Exception/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/%5b%5d-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/CircularDatastructure/cdesc-CircularDatastructure.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Ext/cdesc-Ext.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GeneratorError/cdesc-GeneratorError.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/%5b%5d%3d-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/%5b%5d-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/%7c-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/cdesc-GenericObject.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/dump-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/from_hash-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/json_creatable%3f-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/json_creatable-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/json_create-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/load-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/to_hash-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/GenericObject/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/JSONError/cdesc-JSONError.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/JSONError/wrap-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/MissingUnicodeSupport/cdesc-MissingUnicodeSupport.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/NestingError/cdesc-NestingError.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/ParserError/cdesc-ParserError.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Array/cdesc-Array.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Array/json_transform-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Array/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/FalseClass/cdesc-FalseClass.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/FalseClass/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Float/cdesc-Float.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Float/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Hash/cdesc-Hash.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Hash/json_shift-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Hash/json_transform-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Hash/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Integer/cdesc-Integer.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Integer/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/NilClass/cdesc-NilClass.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/NilClass/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Object/cdesc-Object.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/Object/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/String/Extend/cdesc-Extend.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/String/Extend/json_create-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/String/cdesc-String.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/String/included-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/String/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/String/to_json_raw-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/String/to_json_raw_object-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/TrueClass/cdesc-TrueClass.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/TrueClass/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/GeneratorMethods/cdesc-GeneratorMethods.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/%5b%5d%3d-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/%5b%5d-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/allow_nan%3f-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/array_nl-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/ascii_only%3f-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/cdesc-State.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/check_circular%3f-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/configure-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/depth-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/from_state-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/generate-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/indent-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/max_nesting-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/merge-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/new-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/object_nl-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/quirks_mode%3f-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/quirks_mode-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/space-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/space_before-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/to_h-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/State/to_hash-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Generator/cdesc-Generator.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/Encoding/cdesc-Encoding.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/cdesc-Parser.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/convert_encoding-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/new-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/parse-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/parse_array-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/parse_object-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/parse_string-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/parse_value-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/quirks_mode%3f-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/Parser/reset-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/Pure/cdesc-Pure.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/UnparserError/cdesc-UnparserError.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/cdesc-JSON.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/const_defined_in%3f-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/create_id-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/dump-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/dump_default_options-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/fast_generate-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/generate-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/generator-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/iconv-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/load-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/load_default_options-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/parse%21-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/parse-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/parser-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/pretty_generate-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/recurse_proc-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/restore-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/restore-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/state-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/valid_utf8%3f-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/JSON/valid_utf8%3f-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Kernel/JSON-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Kernel/cdesc-Kernel.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Kernel/j-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Kernel/jj-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/OpenStruct/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/OpenStruct/cdesc-OpenStruct.ri
%{_datadir}/gems/doc/json-1.8.1/ri/OpenStruct/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/OpenStruct/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Range/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Range/cdesc-Range.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Range/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Range/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Rational/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Rational/cdesc-Rational.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Rational/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Rational/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Regexp/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Regexp/cdesc-Regexp.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Regexp/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Regexp/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Struct/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Struct/cdesc-Struct.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Struct/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Struct/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Symbol/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Symbol/cdesc-Symbol.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Symbol/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Symbol/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Time/as_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Time/cdesc-Time.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Time/json_create-c.ri
%{_datadir}/gems/doc/json-1.8.1/ri/Time/to_json-i.ri
%{_datadir}/gems/doc/json-1.8.1/ri/cache.ri
%{_datadir}/gems/doc/json-1.8.1/ri/page-README_rdoc.ri
%{_datadir}/gems/gems/json-1.8.1/README.rdoc
%{_datadir}/gems/gems/json-1.8.1/data/example.json
%{_datadir}/gems/gems/json-1.8.1/data/index.html
%{_datadir}/gems/gems/json-1.8.1/data/prototype.js
%{_datadir}/gems/gems/json-1.8.1/ext/json/ext/generator/extconf.rb
%{_datadir}/gems/gems/json-1.8.1/ext/json/ext/parser/extconf.rb
%{_datadir}/gems/gems/json-1.8.1/install.rb
# %{_datadir}/gems/gems/json-1.8.1/lib/json.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/bigdecimal.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/complex.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/core.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/date.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/date_time.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/exception.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/ostruct.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/range.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/rational.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/regexp.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/struct.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/symbol.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/add/time.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/common.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/ext.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/ext/.keep
%{_datadir}/gems/gems/json-1.8.1/lib/json/generic_object.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/pure.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/pure/generator.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/pure/parser.rb
%{_datadir}/gems/gems/json-1.8.1/lib/json/version.rb
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail1.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail10.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail11.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail12.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail13.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail14.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail18.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail19.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail2.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail20.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail21.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail22.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail23.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail24.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail25.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail27.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail28.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail3.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail4.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail5.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail6.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail7.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail8.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/fail9.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/pass1.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/pass15.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/pass16.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/pass17.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/pass2.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/pass26.json
%{_datadir}/gems/gems/json-1.8.1/tests/fixtures/pass3.json
%{_datadir}/gems/gems/json-1.8.1/tests/setup_variant.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json_addition.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json_encoding.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json_fixtures.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json_generate.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json_generic_object.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json_string_matching.rb
%{_datadir}/gems/gems/json-1.8.1/tests/test_json_unicode.rb
%{_datadir}/gems/gems/json-1.8.1/tools/fuzz.rb
%{_datadir}/gems/gems/json-1.8.1/tools/server.rb
# %{_datadir}/gems/specifications/json-1.8.1.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README.*
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
# %{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*
