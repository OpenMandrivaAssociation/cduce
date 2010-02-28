%define name	cduce
%define version 0.5.3
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XML-oriented functional language
Source:	    http://www.cduce.org/download/%{name}-%{version}.tar.gz
URL:		http://www.cduce.org
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
