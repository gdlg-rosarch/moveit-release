Name:           ros-lunar-moveit-plugins
Version:        0.9.10
Release:        0%{?dist}
Summary:        ROS moveit_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-moveit-fake-controller-manager
Requires:       ros-lunar-moveit-ros-control-interface
Requires:       ros-lunar-moveit-simple-controller-manager
BuildRequires:  ros-lunar-catkin

%description
Metapackage for moveit plugins.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat Dec 09 2017 Michael Görner <me@v4hn.de> - 0.9.10-0
- Autogenerated by Bloom

* Sun Aug 06 2017 Michael Görner <me@v4hn.de> - 0.9.9-0
- Autogenerated by Bloom

* Wed Jun 21 2017 Michael Görner <me@v4hn.de> - 0.9.8-0
- Autogenerated by Bloom

* Mon Jun 05 2017 Michael Görner <me@v4hn.de> - 0.9.7-0
- Autogenerated by Bloom

* Fri May 12 2017 Michael Görner <me@v4hn.de> - 0.9.6-1
- Autogenerated by Bloom

* Wed May 10 2017 Michael Görner <me@v4hn.de> - 0.9.6-0
- Autogenerated by Bloom

