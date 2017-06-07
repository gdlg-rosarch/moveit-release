Name:           ros-indigo-moveit-planners
Version:        0.7.10
Release:        0%{?dist}
Summary:        ROS moveit_planners package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-moveit-planners-ompl
BuildRequires:  ros-indigo-catkin

%description
Metapacakge that installs all available planners for MoveIt

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jun 07 2017 Ioan Sucan <isucan@willowgarage.com> - 0.7.10-0
- Autogenerated by Bloom

* Mon Apr 03 2017 Ioan Sucan <isucan@willowgarage.com> - 0.7.9-0
- Autogenerated by Bloom

* Wed Mar 08 2017 Ioan Sucan <isucan@willowgarage.com> - 0.7.8-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Ioan Sucan <isucan@willowgarage.com> - 0.7.7-0
- Autogenerated by Bloom

* Fri Dec 30 2016 Ioan Sucan <isucan@willowgarage.com> - 0.7.6-0
- Autogenerated by Bloom

* Sun Dec 25 2016 Ioan Sucan <isucan@willowgarage.com> - 0.7.5-0
- Autogenerated by Bloom

* Thu Dec 22 2016 Ioan Sucan <isucan@willowgarage.com> - 0.7.4-0
- Autogenerated by Bloom

* Tue Dec 20 2016 Ioan Sucan <isucan@willowgarage.com> - 0.7.3-0
- Autogenerated by Bloom

