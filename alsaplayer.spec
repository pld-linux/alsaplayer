
Summary:	Alsaplayer - MP2/MP3/WAV/CD player
Summary(pl):	Alsaplayer - odtwarzacz MP2/MP3/WAV/CD
Name:		alsaplayer
Version:	0.99.58
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.alsa-project.org/pub/people/andy/%{name}-%{version}.tar.bz2
Patch0:		%{name}-c++.patch
Requires:	gtk+
BuildRequires:	alsa-lib-devel
BuildRequires:	esound-devel
BuildRequires:	audiofile-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%{_libdir}/%{name}

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
AlsaPlayer is a new type of PCM player. It is heavily multi-threaded
and tries to excercise the ALSA library and driver quite a bit.
Features include:

Input addons:
 - MP2 and MP3 support
 - Ogg Vorbis support
 - WAV support, 8-, 16-bit, mono, stereo, any sample rate
 - CDDA support, CD Digital Audio playback! and thus USB ready :)
 - Also plays files mapped by audiofs (CDDA)
 - MAD MPEG audio
 - Module support (mikmod)

Output addons:
 - ALSA. Best supported of course :)
 - OSS. Kernel native sound drivers
 - Sparc. UltraSparc sound drivers
 - SGI. SGI audio library driver
 - ESD. Enlightened sound daemon support
 - NAS. Network Audio System
 - null :-)

Visual scopes:
 - Stereoscope
 - Monoscope
 - Levelmeter
 - Spacescope
 - FFTscope
 - FFTscope II
 - More being developed...

General features:
 - Full speed (pitch) control, positive *and* negative! (First Linux
   player that does this!! MP3's and CD's do varispeed :)
 - Queue (playlist) support
 - Concurrent visual scopes (open as many as you want)
 - Multi-threaded design for efficient/skip free playback (RT)
 - GUI Interface based on gtk+
 - NOGUI operation for shell script usage
 - Plug-in core architecture
 - Low latency mode, as low as 5ms when scheduled RT
 - Effects stream
 - Software based volume/pan control
 - Accurate scope/audio syncing using ALSA features
 - Portable (well, we'll see about that :)
 - Open source(tm)

%description -l pl
AlsaPlayer to nowy rodzaj odtwarzacza PCM. Jest wielow±tkowy i próbuje
solidnie przeæwiczyæ sterowniki i bibliotekê ALSA. Jego cechy to:

Wej¶cie:
 - obs³uga MP2 i MP3
 - obs³uga Ogg Vorbis
 - obs³uga WAV, 8 i 16-bitowych, mono, stereo, dowolna czêstotliwo¶æ
 - obs³uga CD Digital Audio
 - odtwarzanie plików podmapowanych przez audiofs (CDDA)
 - obs³uga MAD - MPEG Audio
 - obs³uga modu³ów (mikmod)

Wyj¶cie:
 - ALSA - oczywi¶cie najlepiej obs³ugiwana :)
 - OSS - natywne sterowniki z j±dra
 - Sparc - sterowniki d¼wiêku dla UltraSparca
 - SGI - biblioteka sterowników d¼wiêku SGI
 - ESD - obs³uga O¶wieconego demona d¼wiêku
 - NAS - Sieciowego Systemu Audio
 - null :-)

Wizualizacja:
 - Stereoskop
 - Monoskop
 - Wska¼nik poziomu d¼wiêku
 - inne, wkrótce wiêcej...

Ogólne cechy:
 - Kontrola szybko¶ci (w obie strony)
 - obs³uga kolejki (playlisty)
 - obs³uga wielu wska¼ników naraz
 - wielow±tkowo¶æ
 - interfejs graficzny bazuj±cy na gtk+
 - operacje bez GUI na potrzeby skryptów
 - architektura wtyczek
 - programowa kontrola g³o¶no¶ci i balansu
 - synchronizacja d¼wiêku i wska¼ników przy u¿yciu mo¿liwo¶ci ALSA

%prep
%setup -q
#%patch0 -p1

%build
libtoolize --copy --force
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/alsaplayer
%{_pkglibdir}
