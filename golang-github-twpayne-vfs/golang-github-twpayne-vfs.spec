# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/twpayne/go-vfs
%global goipath         github.com/twpayne/go-vfs
Version:                4.1.0

%gometa

%global common_description %{expand:
Package vfs provides an abstraction of the os and io packages that is easy to
test.}

%global goaltipaths     github.com/twpayne/go-vfs/v3
%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package vfs provides an abstraction of the os and io packages that is easy to test

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
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 4.1.0-1
- Initial package
