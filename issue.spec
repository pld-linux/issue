Summary:	PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(fr):	Fichier de version de PLD Linux.
Summary(pl):	Wersja Linuxa PLD.
Summary(tr):	PLD Linux s�r�m dosyas�
Name:		issue
Version:	1.0
Release:	2
Copyright:	free
Group:		Base
Group(pl):	Podstawowe
Buildarch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
PLD Linux release file

%description -l de
PLD Linux Release-Datei

%description -l fr
Fichier de version de PLD Linux.

%description
Wersja Linuxa PLD.

%description -l tr
PLD Linux s�r�m dosyas�

%install
install -d $RPM_BUILD_ROOT/etc
 
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/pld-release
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/issue
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/issue.net
echo "Kernel \r on an \m" >> $RPM_BUILD_ROOT/etc/issue
echo "Kernel %r on an %m" >> $RPM_BUILD_ROOT/etc/issue.net

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/etc/pld-release
%config(noreplace) /etc/issue*

%changelog
* Thu Jun 24 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.0-2]
- build for PLD-stable
- removed Source
- separate issue and issue.net

* Tue Dec 08 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
   [1.1-1d]
-  build for prerelease-1.
