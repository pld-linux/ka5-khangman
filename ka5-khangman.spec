#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		khangman
Summary:	khangman
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4103eb08f087a5aa9f512c73b0efe866
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	ka5-libkeduvocdocument-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KHangMan is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears.
After 10 tries, if the word is not guessed, the game is over and the
answer is displayed.

%description -l pl.UTF-8
KHangMan to klasyczna gra w wisielca. Dziecko ma odgadnąć słowo,
literka po literce. Przy każdym pudle jest rysowane fragment obrazka
wisielca. Po 10 próbach, jeśli słowo nie zostało odgadnięte, gra się
kończy i wyświetlana jest prawidłowa odpowiedź.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications/Games
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/etc/xdg/khangman.knsrc
%attr(755,root,root) %{_bindir}/khangman

%files data  -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/org.kde.khangman.desktop
%{_datadir}/config.kcfg/khangman.kcfg
%{_iconsdir}/hicolor/128x128/apps/khangman.png
%{_iconsdir}/hicolor/16x16/apps/khangman.png
%{_iconsdir}/hicolor/22x22/apps/khangman.png
%{_iconsdir}/hicolor/32x32/apps/khangman.png
%{_iconsdir}/hicolor/48x48/apps/khangman.png
%{_iconsdir}/hicolor/64x64/apps/khangman.png
%{_iconsdir}/hicolor/scalable/apps/khangman.svgz
%{_datadir}/khangman
%lang(ca) %{_mandir}/ca/man6/khangman.6*
%lang(de) %{_mandir}/de/man6/khangman.6*
%lang(es) %{_mandir}/es/man6/khangman.6*
%lang(et) %{_mandir}/et/man6/khangman.6*
%lang(it) %{_mandir}/it/man6/khangman.6*
%lang(C) %{_mandir}/man6/khangman.6*
%lang(nl) %{_mandir}/nl/man6/khangman.6*
%lang(pt) %{_mandir}/pt/man6/khangman.6*
%lang(pt_BR) %{_mandir}/pt_BR/man6/khangman.6*
%lang(ru) %{_mandir}/ru/man6/khangman.6*
%lang(sv) %{_mandir}/sv/man6/khangman.6*
%lang(uk) %{_mandir}/uk/man6/khangman.6*
%lang(fr) %{_mandir}/fr/man6/khangman.6*
%{_datadir}/metainfo/org.kde.khangman.appdata.xml
