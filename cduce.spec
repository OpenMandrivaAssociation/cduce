%define name	cduce
%define version	0.4.2
%define release	%mkrel 1
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XML-oriented functional language
Source0:	http://www.cduce.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-0.4.1-destdir.patch
URL:		http://www.cduce.org
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-ulex-devel
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	ocaml-pxp-devel >= 1.1.96
BuildRequires:	findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CDuce is a modern XML-oriented functional language with innovative features. A
compiler is available under the terms of an open-source license. CDuce is
type-safe, efficient, and offer powerful constructions to work with XML
documents.

%prep
%setup -q
%patch0 -p1 -b .destdir

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --docdir=%{_docdir}/%{name}-%{version}
%make

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}/%{ocaml_sitelib}
install -d -m755 %{buildroot}/%{ocaml_sitelib}/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}" DESTDIR="%{buildroot}"
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.so.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/*
%{_mandir}/man1/*
%{ocaml_sitelib}/cduce
