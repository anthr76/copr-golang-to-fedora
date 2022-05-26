# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/go-git/gcfg
%global goipath         github.com/go-git/gcfg
Version:                1.5.0

%gometa

%global common_description %{expand:
Go-gcfg/gcfg fork for usage in src-d/go-git.}

%global golicenses      LICENSE
%global godocs          README

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go-gcfg/gcfg fork for usage in src-d/go-git

# Upstream license specification: BSD-3-Clause
License:        BSD
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
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 1.5.0.2
- Disable checks

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 1.5.0-1
- Initial package
