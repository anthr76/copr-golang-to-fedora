# Generated by go2rpm 1.6.0
%bcond_with check

# https://github.com/go-git/go-git
%global goipath         github.com/go-git/go-git
Version:                5.4.2

%gometa

%global common_description %{expand:
A highly extensible Git implementation in pure Go.}

%global golicenses      LICENSE
%global godocs          _examples CODE_OF_CONDUCT.md COMPATIBILITY.md\\\
                        CONTRIBUTING.md README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        A highly extensible Git implementation in pure Go

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

%build
for cmd in cli/go-git; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc _examples CODE_OF_CONDUCT.md COMPATIBILITY.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.4.2-5
- Generate build requires

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.4.2-4
- Fix macro ordering

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.4.2-3
- Add manual build requires for go-billy

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.4.2-2
- Disable tests for failures on golang-x-crypto

* Wed May 25 2022 Anthony Rabbito <hello@anthonyrabbito.com> - 5.4.2-1
- Initial package
