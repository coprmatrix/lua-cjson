%define luarocks_pkg_name lua-cjson
%define luarocks_pkg_version 2.1.0.14-1
%define luarocks_pkg_prefix lua-cjson-2.1.0.14-1
%define luarocks_pkg_major 2.1.0.14
%define luarocks_pkg_minor 1
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true

Name: lua-cjson
BuildRequires: lua-rpm-macros

BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: make
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: A fast JSON encoding/parsing module
License: MIT
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
Requires: %{luadist lua >= 5.1}

Source0: lua-cjson-2.1.0.14-1.tar.gz
Source1: lua-cjson-2.1.0.14-1.rockspec
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
        The Lua CJSON module provides JSON support for Lua. It features:
        - Fast, standards compliant encoding/parsing routines
        - Full support for JSON with UTF-8, including decoding surrogate pairs
        - Optional run-time support for common exceptions to the JSON specification
          (infinity, NaN,..)
        - No dependencies on other libraries
    

%prep
%autosetup -p1 -n %luarocks_pkg_prefix
%luarocks_prep

%generate_buildrequires

%build
%{?luarocks_subpackages_build}
%{!?luarocks_subpackages_build:%luarocks_build}

%install
%{?luarocks_subpackages_install}
%{!?luarocks_subpackages_install:%luarocks_install %{luarocks_pkg_prefix}.*.rock}
%{?lua_generate_file_list}
%check
%if %{with check}
%{?luarocks_check}
%endif
%post %{?lua_scriplets}
update-alternatives --install %{_bindir}/json2lua json2lua %{luarocks_treedir}/%{luarocks_pkg_name}/%{luarocks_pkg_version}/bin/json2lua 25
update-alternatives --install %{_bindir}/lua2json lua2json %{luarocks_treedir}/%{luarocks_pkg_name}/%{luarocks_pkg_version}/bin/lua2json 25
%postun %{?lua_scriplets}
update-alternatives --remove json2lua %{luarocks_treedir}/%{luarocks_pkg_name}/%{luarocks_pkg_version}/bin/json2lua
update-alternatives --remove lua2json %{luarocks_treedir}/%{luarocks_pkg_name}/%{luarocks_pkg_version}/bin/lua2json

%files %{?lua_files}%{!?lua_files:-f lua_files.list}
%dir %lua_noarchdir
%dir %lua_archdir
%dir %lua_noarchdir/cjson
%dir %lua_archdir/cjson
