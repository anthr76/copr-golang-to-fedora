# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/twpayne/go-xdg
%global goipath         github.com/twpayne/go-xdg
Version:                6.0.0

%gometa

%global common_description %{expand:
Package xdg provides support for the XDG Base Directory Specification.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Package xdg provides support for the XDG Base Directory Specification

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 6.0.0-5
- Enable tests and generate BuildRequires

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 6.0.0-4
- Disable tests since it's trying to pull github.com/twpayne/go-vfs/v3/vfs

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 6.0.0-3
- Remove automatic macros

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 6.0.0-2
- Add manual BuildRequires

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 6.0.0-1
- Initial package
