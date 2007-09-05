#
# Conditional build
%bcond_without	esound		# build without esound plugin
%bcond_without	flac		# build without FLAC plugin
%bcond_without	jack		# build without jack plugin
%bcond_without	mikmod		# build without mikmod plugin
%bcond_without	nas		# build without nas plugin
#
Summary:	Alsaplayer - CD/FLAC/MOD/MP3/Ogg/WAV player
Summary(pl.UTF-8):	Alsaplayer - odtwarzacz CD/FLAC/MOD/MP3/Ogg/WAV
Name:		alsaplayer
Version:	0.99.80
%define	pre	rc2
Release:	0.%{pre}.1
License:	GPLv3
Group:		Applications/Sound
Source0:	http://www.alsaplayer.org/%{name}-%{version}-%{pre}.tar.bz2
# Source0-md5:	bc8325c704f6cad167236055e1ff3ebb
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-docs.patch
Patch1:		%{name}-flac.patch
URL:		http://www.alsaplayer.org/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esound:BuildRequires:	esound-devel >= 0.2.4}
%{?with_flac:BuildRequires:	flac-c++-devel >= 1.2.0}
BuildRequires:	gtk+2-devel >= 1:2.0.3
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.69.1}
%{?with_flac:BuildRequires:	libid3tag-devel}
BuildRequires:	libmad-devel
%{?with_mikmod:BuildRequires:	libmikmod-devel}
BuildRequires:	libsndfile-devel >= 1.0.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
BuildRequires:	xosd-devel
Requires(post):	/sbin/ldconfig
Requires:	alsaplayer_output
Requires:	alsaplayer_ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_pkglibdir	%{_libdir}/%{name}

%description
AlsaPlayer is a new type of PCM player. It is heavily multi-threaded
and tries to exercise the ALSA library and driver quite a bit.
Features include:

Input addons:
- MP2 and MP3 support
- Ogg Vorbis support (subpackage)
- WAV support, 8-, 16-bit, mono, stereo, any sample rate
- CDDA support, CD Digital Audio playback! and thus USB ready :)
- Also plays files mapped by audiofs (CDDA)
- MAD MPEG audio
- Module support (mikmod) (subpcakage)
- FLAC support

Output addons:
- ALSA. Best supported of course :) (subpackage)
- OSS. Kernel native sound drivers
- Sparc. UltraSparc sound drivers
- SGI. SGI audio library driver
- ESD. Enlightened sound daemon support (subpackage)
- NAS. Network Audio System (subpakcage)
- low latency JACK output
- null :-)

Visual scopes:
- Stereoscope
- Monoscope
- Levelmeter
- Spacescope
- FFTscope
- FFTscope II
- Spectrum GL

General features:
- Full speed (pitch) control, positive *and* negative! (First Linux
  player that does this!! MP3's and CD's do varispeed :)
- Queue (playlist) support
- Concurrent visual scopes (open as many as you want)
- Multi-threaded design for efficient/skip free playback (RT)
- GUI Interface based on GTK+
- NOGUI operation for shell script usage
- On-screen-display based on xosd
- Plug-in core architecture
- Low latency mode, as low as 5ms when scheduled RT
- Effects stream
- Software based volume/pan control
- Accurate scope/audio syncing using ALSA features

%description -l pl.UTF-8
AlsaPlayer to nowy rodzaj odtwarzacza PCM. Jest wielowątkowy i próbuje
solidnie przećwiczyć sterowniki i bibliotekę ALSA. Jego cechy to:

Wejście:
- obsługa MP2 i MP3
- obsługa Ogg Vorbis (w podpakiecie)
- obsługa WAV, 8 i 16-bitowych, mono, stereo o dowolnej częstotliwości
- obsługa CD Digital Audio
- odtwarzanie plików podmapowanych przez audiofs (CDDA)
- obsługa MAD - MPEG Audio
- obsługa modułów (mikmod) (w podpakiecie)
- obsług bezstratnej kompresji dźwięku FLAC

Wyjście:
- OSS - natywne sterowniki z jądra
- ALSA - oczywiście najlepiej obsługiwana :) (w podpakiecie)
- Sparc - sterowniki dźwięku dla UltraSparca
- SGI - biblioteka sterowników dźwięku SGI
- ESD - obsługa Oświeconego demona dźwięku (w podpakiecie)
- NAS - Sieciowego Systemu Audio (w podpakiecie)
- JACK - zestaw połączeń dźwięku o małych opóźnieniach (w podpakiecie)
- null :-)

Wizualizacja:
- Stereoskop
- Monoskop
- Wskaźnik poziomu dźwięku
- Wskaźniki oparte o analizę FFT
- analizator spektrum sygnału w oparciu o OpenGL

Ogólne cechy:
- Kontrola szybkości (w obie strony)
- obsługa kolejki (playlisty)
- obsługa wielu wskaźników naraz
- wielowątkowość
- interfejs graficzny bazujący na GTK+
- operacje bez GUI na potrzeby skryptów
- tryb Informacje-na-ekranie oparty o xosd
- architektura wtyczek
- tryb "czasu rzeczywistego" dający opóźnienia rzędu 5ms
- programowa kontrola głośności i balansu
- synchronizacja dźwięku i wskaźników przy użyciu możliwości ALSA

%package daemon
Summary:	Deamon interface for Alsaplayer
Summary(pl.UTF-8):	Interfejs demona alsaplayera
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description daemon
Deamon interface for Alsaplayer.

%description daemon -l pl.UTF-8
Interfejs demona alsaplayera.

%package input-audiofile
Summary:	Alsaplayer plugin for playing WAVE audio formats using audiofile
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania plików audio typu WAVE przy użyciu audiofile
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-audiofile
Alsaplayer plugin for playing WAVE audio formats (like AIFF, AIFC,
WAVE, ...) using audiofile library.

%description input-audiofile -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania plików audio typu WAVE (AIFF,
AIFC, WAVE, ...) przy użyciu biblioteki audiofile.

%package input-flac
Summary:	Alsaplayer plugin for playing FLAC files
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania plików FLAC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-flac
Alsaplayer plugin for playing FLAC files.

%description input-flac -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania plików FLAC.

%package input-mad
Summary:	Alsaplayer plugin for playing MP3 files using MAD
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania plików MP3 przy pomocy MAD
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-mad
Alsaplayer plugin for playing MP3 files using MAD.

%description input-mad -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania plików MP3 przy pomocy MAD.

%package input-mikmod
Summary:	Alsaplayer plugin for playing mod files
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania plików mod
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-mikmod
Alsaplayer plugin for playing mod files.

%description input-mikmod -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania plików mod.

%package input-sndfile
Summary:	Alsaplayer plugin for playing WAVE audio formats using libsndfile
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania plików audio typu WAVE przy użyciu libsndfile
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-sndfile
Alsaplayer plugin for playing WAVE audio formats (like AIFF, AIFC,
WAVE, ...) using libsndfile library.

%description input-sndfile -l pl.UTF-8
Wtyczka do alsaplayera do odtwarzania plików audio typu WAVE (AIFF,
AIFC, WAVE, ...) przy użyciu biblioteki libsndfile.

%package input-vorbis
Summary:	Alsaplayer plugin for playing Ogg/Vorbis files
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania plików Ogg/Vorbis
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-vorbis
Alsaplayer plugin for playing Ogg/Vorbis files.

%description input-vorbis -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania plików Ogg/Vorbis.

%package interface-gtk2
Summary:	GTK+ 2 interface for Alsaplayer
Summary(pl.UTF-8):	Interfejs GTK+ 2 alsaplayera
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	alsaplayer_ui

%description interface-gtk2
GTK+ 2 interface for Alsaplayer.

%description interface-gtk2 -l pl.UTF-8
Interfejs GTK+2 alsaplayera.

%package interface-text
Summary:	Text interface for Alsaplayer
Summary(pl.UTF-8):	Interfejs tekstowy alsaplayera
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	alsaplayer_ui

%description interface-text
Text interface for Alsaplayer.

%description interface-text -l pl.UTF-8
Interfejs tekstowy alsaplayera.

%package interface-xosd
Summary:	xosd interface for Alsaplayer
Summary(pl.UTF-8):	Interfejs xosd alsaplayera
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	alsaplayer_ui

%description interface-xosd
xosd interface for Alsaplayer.

%description interface-xosd -l pl.UTF-8
Interfejs xosd alsaplayera.

%package output-alsa
Summary:	Alsaplayer plugin for playing through alsa drivers
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania przez sterowniki alsa
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	alsaplayer_output

%description output-alsa
Alsaplayer plugin for playing sound through alsa drivers.

%description output-alsa -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania dźwięku przez sterowniki alsa.

%package output-esound
Summary:	Alsaplayer plugin for playing through esound daemon
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania przez demona esound
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	alsaplayer_output

%description output-esound
Alsaplayer plugin for playing sound through esound daemon.

%description output-esound -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania dźwięku przez demona esound.

%package output-nas
Summary:	Alsaplayer plugin for playing through NAS daemon
Summary(pl.UTF-8):	Wtyczka do alsaplayera do odtwarzania przez demona NAS
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	alsaplayer_output

%description output-nas
Alsaplayer plugin for playing sound through NAS (network audio system)
daemon.

%description output-nas -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania dźwięku przez demona NAS (network
audio system).

%package output-jack
Summary:	Alsaplayer plugin for playing sound through JACK
Summary(pl.UTF-8):	Wtyczka alsaplayera do odtwarzania dźwięku przez JACK-a
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	alsaplayer_output

%description output-jack
Alsaplayer plugin for sound through JACK system.

%description output-jack -l pl.UTF-8
Wtyczka alsaplayera do odtwarzania dźwięku przez system JACK.

%package scopes2-gtk
Summary:	Alsaplayer plugins for visualization
Summary(pl.UTF-8):	Wtyczki alsaplayera do wizualizacji
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Obsoletes:	alsaplayer-scopes-gtk

%description scopes2-gtk
Alsaplayer plugins for visualization.

%description scopes2-gtk -l pl.UTF-8
Wtyczki do alsaplayera do wizualizacji.

%package scopes2-opengl
Summary:	Alsaplayer plugin for visualization using OpenGL
Summary(pl.UTF-8):	Wtyczka alsaplayera do wizualizacji z użyciem OpenGL
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	alsaplayer-scopes-opengl

%description scopes2-opengl
Alsaplayer plugin for visualization using OpenGL.

%description scopes2-opengl -l pl.UTF-8
Wtyczka do alsaplayera do wizualizacji z użyciem OpenGL.

%package devel
Summary:	Alsaplayer header files
Summary(pl.UTF-8):	Pliki nagłówkowe Alsaplayera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Alsaplayer library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Alsaplayera.

%package static
Summary:	Alsaplayer static library
Summary(pl.UTF-8):	Biblioteka statyczna Alsaplayera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Alsaplayer static library.

%description static -l pl.UTF-8
Biblioteka statyczna Alsaplayera.

%prep
%setup -q -n %{name}-%{version}-%{pre}
%patch0 -p1
#patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS=" -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
export CPPFLAGS LDFLAGS
%configure \
	%{?with_esound:--en}%{!?with_esound:--dis}able-esd \
	%{?with_flac:--en}%{!?with_flac:--dis}able-flac \
	%{?with_flac:--en}%{!?with_flac:--dis}able-oggflac \
	%{?with_jack:--en}%{!?with_jack:--dis}able-jack \
	%{?with_mikmod:--en}%{!?with_mikmod:--dis}able-mikmod \
	%{?with_nas:--en}%{!?with_nas:--dis}able-nas \
	%{?with_esound:--en}%{!?with_esound:--dis}able-esd \
	--enable-alsa \
	--enable-audiofile \
	--enable-gtk2 \
	--enable-oggflac \
	--enable-oggvorbis \
	--enable-opengl \
	--enable-oss \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_pkglibdir}/input/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/interface/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/output/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/reader/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/scopes2/*.{a,la}

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
echo
echo "Remember to install appropriate alsaplayer-input-* plugins"
echo "for files you want to play, for example:"
echo "alsaplayer-input-mad to play MP3s."
echo

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/alsaplayer
%attr(755,root,root) %{_libdir}/libalsaplayer.so.0.0.2
%dir %{_pkglibdir}
%dir %{_pkglibdir}/input
%dir %{_pkglibdir}/interface
%dir %{_pkglibdir}/output
%dir %{_pkglibdir}/reader
%dir %{_pkglibdir}/scopes2
%attr(755,root,root) %{_pkglibdir}/input/libcdda.so
%attr(755,root,root) %{_pkglibdir}/input/libwav.so
%attr(755,root,root) %{_pkglibdir}/output/liboss_out.so
%attr(755,root,root) %{_pkglibdir}/output/libnull_out.so
%attr(755,root,root) %{_pkglibdir}/reader/libfile.so
%attr(755,root,root) %{_pkglibdir}/reader/libhttp.so
%{_mandir}/man*/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files daemon
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libdaemon_interface.so

%files interface-gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libgtk2_interface.so

%files interface-text
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libtext_interface.so

%files interface-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libxosd_interface.so

%files input-audiofile
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libaf.so

%if %{with flac}
%files input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libflac_in.so
%endif

%files input-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libmad_in.so

%if %{with mikmod}
%files input-mikmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libmod.so
%endif

%files input-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libsndfile_in.so

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libvorbis_in.so

%files output-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libalsa_out.so

%if %{with esound}
%files output-esound
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libesound_out.so
%endif

%if %{with jack}
%files output-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libjack_out.so
%endif

%if %{with nas}
%files output-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libnas_out.so
%endif

%files scopes2-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/scopes2/libblurscope.so
%attr(755,root,root) %{_pkglibdir}/scopes2/liblevelmeter.so
%attr(755,root,root) %{_pkglibdir}/scopes2/liblogbarfft.so
%attr(755,root,root) %{_pkglibdir}/scopes2/libmonoscope.so
%attr(755,root,root) %{_pkglibdir}/scopes2/libspacescope.so
%attr(755,root,root) %{_pkglibdir}/scopes2/libsynaescope.so

%files scopes2-opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/scopes2/liboglspectrum.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libalsaplayer.so
%{_libdir}/libalsaplayer.la
%{_includedir}/alsaplayer
%{_pkgconfigdir}/alsaplayer.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libalsaplayer.a
