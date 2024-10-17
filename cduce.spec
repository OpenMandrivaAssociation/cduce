%define name	cduce
%define version 0.5.3
%define release	4

Name:		%{name}
Version:	0.5.5
Release:	2
Summary:	XML-oriented functional language
Source:	    http://www.cduce.org/download/%{name}-%{version}.tar.gz
URL:		https://www.cduce.org
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	ocaml-sources
BuildRequires:	camlp4
BuildRequires:	ocaml-expat-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-ulex-devel
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	ocaml-curl-devel
BuildRequires:	ocaml-pxp-devel >= 1.1.96
BuildRequires:	ocaml-findlib
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
CDuce is a modern XML-oriented functional language with innovative features. A
compiler is available under the terms of an open-source license. CDuce is
type-safe, efficient, and offer powerful constructions to work with XML
documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --docdir=%{_docdir}/%{name} \
    --mliface=%{_prefix}/src/ocaml
make all doc VERBOSE=true

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
make install \
    OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml \
    BINDIR=%{buildroot}%{_bindir} \
    MANDIR=%{buildroot}%{_mandir} \
    DOCDIR=%{buildroot}%{_docdir}/%{name} \

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/ocaml/cduce
%exclude %{_libdir}/ocaml/cduce/*.a
%exclude %{_libdir}/ocaml/cduce/*.cmxa

%files devel
%defattr(-,root,root,-)
%{_libdir}/ocaml/cduce/*.a
%{_libdir}/ocaml/cduce/*.cmxa


%changelog
* Sun Feb 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-3mdv2010.1
+ Revision: 512708
- rebuild

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-2mdv2010.0
+ Revision: 390543
- rebuild for latest ocaml

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-1mdv2010.0
+ Revision: 384005
- new version
- drop patch, merged upstream

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2.1-2mdv2009.1
+ Revision: 321204
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore
- fix build with latest ocaml (fedora patch)
- add curl support

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2.1-1mdv2009.0
+ Revision: 272368
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-5mdv2009.0
+ Revision: 243470
- rebuild

* Fri Mar 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-3mdv2008.1
+ Revision: 181374
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-2mdv2008.0
+ Revision: 80935
- fix build dependencies
- build ocaml interface
  expat support

* Sat Aug 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 65397
- new version

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - new release: 0.4.2


* Fri Feb 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-1mdv2007.0
+ Revision: 124865
- fix build dependencies

* Fri Feb 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-1mdv2007.1
- first mdv release


