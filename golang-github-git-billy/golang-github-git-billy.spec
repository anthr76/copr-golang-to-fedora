# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/go-git/go-billy
%global goipath         github.com/go-git/go-billy
Version:                5.3.1

%gometa

%global goaltipaths     github.com/go-git/go-billy/v5
%global common_description %{expand:
The missing interface filesystem abstraction for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        The missing interface filesystem abstraction for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-5
- Set goaltipaths

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-4
- Enable tests

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-4
- Don't use v5 in the package name

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-3
- Use v5 in the package name

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-2
- Disable checks

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.3.1-1
- Initial package
